import fs from "fs";
import path from "path";

// ─── Types ───────────────────────────────────────────────────────────────────

export interface ProblemMeta {
    month: number;
    week: number;
    day: number;
    slug: string; // e.g. "day-1-the-modular-operator"
    title: string; // e.g. "The Modular Operator"
    fileName: string; // e.g. "week1-day1-the-modular-operator.py"
    filePath: string; // absolute path to the .py file
    href: string; // e.g. "/month-1/week-1/day-1-the-modular-operator"
}

export interface ParsedSections {
    problemStatement: string;
    intuition: string;
    approach: string;
    timeComplexity: string;
    spaceComplexity: string;
    commonMistakes: string;
    finalThoughts: string;
    code: string;
}

export interface WeekData {
    week: number;
    problems: ProblemMeta[];
}

export interface MonthData {
    month: number;
    weeks: WeekData[];
}

// ─── Helpers ─────────────────────────────────────────────────────────────────

function extractNumber(name: string, prefix: string): number {
    const match = name.match(new RegExp(`${prefix}(\\d+)`));
    return match ? parseInt(match[1], 10) : 0;
}

function slugFromFileName(fileName: string): string {
    // week1-day1-the-modular-operator.py → day-1-the-modular-operator
    const withoutExt = fileName.replace(/\.py$/, "");
    const match = withoutExt.match(/week\d+-day(\d+)-(.+)/);
    if (!match) return withoutExt;
    return `day-${match[1]}-${match[2]}`;
}

function titleFromSlug(slug: string): string {
    // day-1-the-modular-operator → The Modular Operator
    const match = slug.match(/^day-\d+-(.+)$/);
    if (!match) return slug;
    return match[1]
        .split("-")
        .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
        .join(" ");
}

// ─── Core Functions ──────────────────────────────────────────────────────────

const PROBLEMS_DIR = path.join(process.cwd(), "problems");

/**
 * Walk the problems directory and return a structured tree:
 *   Month[] → Week[] → Problem[]
 * Everything is sorted numerically ascending.
 */
export function parsePracticeStructure(): MonthData[] {
    if (!fs.existsSync(PROBLEMS_DIR)) return [];

    const months = fs
        .readdirSync(PROBLEMS_DIR)
        .filter((d) => fs.statSync(path.join(PROBLEMS_DIR, d)).isDirectory())
        .sort((a, b) => extractNumber(a, "month") - extractNumber(b, "month"));

    return months.map((monthDir) => {
        const monthNum = extractNumber(monthDir, "month");
        const monthPath = path.join(PROBLEMS_DIR, monthDir);

        const weeks = fs
            .readdirSync(monthPath)
            .filter((d) => fs.statSync(path.join(monthPath, d)).isDirectory())
            .sort((a, b) => extractNumber(a, "week") - extractNumber(b, "week"));

        return {
            month: monthNum,
            weeks: weeks.map((weekDir) => {
                const weekNum = extractNumber(weekDir, "week");
                const weekPath = path.join(monthPath, weekDir);

                const files = fs
                    .readdirSync(weekPath)
                    .filter((f) => f.endsWith(".py"))
                    .sort((a, b) => {
                        const dayA = extractNumber(a, "day");
                        const dayB = extractNumber(b, "day");
                        return dayA - dayB;
                    });

                return {
                    week: weekNum,
                    problems: files.map((fileName) => {
                        const slug = slugFromFileName(fileName);
                        const dayNum = extractNumber(fileName, "day");
                        return {
                            month: monthNum,
                            week: weekNum,
                            day: dayNum,
                            slug,
                            title: titleFromSlug(slug),
                            fileName,
                            filePath: path.join(weekPath, fileName),
                            href: `/month-${monthNum}/week-${weekNum}/${slug}`,
                        };
                    }),
                };
            }),
        };
    });
}

/**
 * Flatten the tree into a single sorted array of all problems.
 */
export function flattenProblems(): ProblemMeta[] {
    const tree = parsePracticeStructure();
    const flat: ProblemMeta[] = [];
    for (const month of tree) {
        for (const week of month.weeks) {
            flat.push(...week.problems);
        }
    }
    return flat;
}

/**
 * Get all problems (alias for flattenProblems).
 */
export function getAllProblems(): ProblemMeta[] {
    return flattenProblems();
}

/**
 * Given a slug, return {previous, next} problem metadata.
 * Returns null for boundaries.
 */
export function getPreviousNext(slug: string): {
    previous: ProblemMeta | null;
    next: ProblemMeta | null;
} {
    const all = flattenProblems();
    const idx = all.findIndex((p) => p.slug === slug);
    if (idx === -1) return { previous: null, next: null };
    return {
        previous: idx > 0 ? all[idx - 1] : null,
        next: idx < all.length - 1 ? all[idx + 1] : null,
    };
}

/**
 * Find a single problem by its slug.
 */
export function getProblemBySlug(slug: string): ProblemMeta | undefined {
    return flattenProblems().find((p) => p.slug === slug);
}

// ─── Python File Parsing ─────────────────────────────────────────────────────

/**
 * Parse a Python file and extract structured sections.
 * Supports both triple-quoted docstrings and # comment blocks.
 */
export function parsePythonFile(filePath: string): ParsedSections {
    const content = fs.readFileSync(filePath, "utf-8");

    // Try triple-quoted docstring first
    const docstringMatch = content.match(
        /^"""([\s\S]*?)"""/m
    );

    let sections: ParsedSections = {
        problemStatement: "",
        intuition: "",
        approach: "",
        timeComplexity: "",
        spaceComplexity: "",
        commonMistakes: "",
        finalThoughts: "",
        code: "",
    };

    if (docstringMatch) {
        const docstring = docstringMatch[1];
        sections = parseDocstringSections(docstring);
    } else {
        // Fall back to # comment parsing
        sections = parseCommentSections(content);
    }

    // Extract code (everything after the docstring or comment header)
    sections.code = extractCode(content);

    return sections;
}

function parseDocstringSections(docstring: string): ParsedSections {
    const sections: ParsedSections = {
        problemStatement: "",
        intuition: "",
        approach: "",
        timeComplexity: "",
        spaceComplexity: "",
        commonMistakes: "",
        finalThoughts: "",
        code: "",
    };

    const sectionMap: Record<string, keyof ParsedSections> = {
        "problem statement": "problemStatement",
        "intuition": "intuition",
        "approach": "approach",
        "time complexity": "timeComplexity",
        "space complexity": "spaceComplexity",
        "common mistakes": "commonMistakes",
        "final thoughts": "finalThoughts",
    };

    let currentKey: keyof ParsedSections | null = null;
    const lines = docstring.split("\n");

    for (const line of lines) {
        const trimmed = line.trim();
        const headerMatch = trimmed.match(/^(.+?):\s*$/);

        if (headerMatch) {
            const headerLower = headerMatch[1].toLowerCase().trim();
            if (sectionMap[headerLower]) {
                currentKey = sectionMap[headerLower];
                continue;
            }
        }

        if (currentKey && trimmed) {
            sections[currentKey] += (sections[currentKey] ? "\n" : "") + trimmed;
        }
    }

    return sections;
}

function parseCommentSections(content: string): ParsedSections {
    // For files without docstrings, extract the leading comments as problem statement
    const lines = content.split("\n");
    const commentLines: string[] = [];
    for (const line of lines) {
        const trimmed = line.trim();
        if (trimmed.startsWith("#")) {
            commentLines.push(trimmed.replace(/^#\s*/, ""));
        } else if (trimmed === "") {
            if (commentLines.length > 0) commentLines.push("");
        } else {
            break;
        }
    }

    return {
        problemStatement: commentLines.join("\n").trim(),
        intuition: "",
        approach: "",
        timeComplexity: "",
        spaceComplexity: "",
        commonMistakes: "",
        finalThoughts: "",
        code: "",
    };
}

function extractCode(content: string): string {
    // Remove the docstring if present
    const withoutDocstring = content.replace(/^"""[\s\S]*?"""\n*/m, "");

    // Remove leading comment block
    const lines = withoutDocstring.split("\n");
    let codeStart = 0;
    let inLeadingComments = true;

    for (let i = 0; i < lines.length; i++) {
        const trimmed = lines[i].trim();
        if (inLeadingComments) {
            if (trimmed.startsWith("#") || trimmed === "") {
                continue;
            } else {
                codeStart = i;
                inLeadingComments = false;
                break;
            }
        }
    }

    return lines.slice(codeStart).join("\n").trim();
}
