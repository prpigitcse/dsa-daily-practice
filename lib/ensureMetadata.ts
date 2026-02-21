/**
 * ensureMetadata.ts
 *
 * Build-time script that scans every .py file in /problems/
 * and injects a placeholder docstring if the required
 * triple-quoted docstring is missing.
 *
 * Run: npx tsx lib/ensureMetadata.ts
 * Or via: npm run ensure-metadata
 */

import fs from "fs";
import path from "path";

const PROBLEMS_DIR = path.join(process.cwd(), "problems");

const PLACEHOLDER_DOCSTRING = `"""
Problem Statement:
<Add clear problem description>

Intuition:
<Explain reasoning>

Approach:
<Step-by-step method>

Time Complexity:
O(?)

Space Complexity:
O(?)

Common Mistakes:
- <Add common mistakes>

Final Thoughts:
<Add final thoughts>
"""

`;

function walkPyFiles(dir: string): string[] {
    const results: string[] = [];
    if (!fs.existsSync(dir)) return results;

    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);
        if (entry.isDirectory()) {
            results.push(...walkPyFiles(fullPath));
        } else if (entry.name.endsWith(".py")) {
            results.push(fullPath);
        }
    }
    return results;
}

function hasDocstring(content: string): boolean {
    return /^"""/m.test(content);
}

function ensureMetadata(): void {
    const files = walkPyFiles(PROBLEMS_DIR);
    let updated = 0;

    for (const filePath of files) {
        const content = fs.readFileSync(filePath, "utf-8");

        if (!hasDocstring(content)) {
            const newContent = PLACEHOLDER_DOCSTRING + content;
            fs.writeFileSync(filePath, newContent, "utf-8");
            updated++;
            console.log(`✅ Injected docstring: ${path.relative(process.cwd(), filePath)}`);
        }
    }

    if (updated === 0) {
        console.log("✅ All files already have docstrings.");
    } else {
        console.log(`\n✅ Updated ${updated} file(s).`);
    }
}

ensureMetadata();
