import type { Metadata } from "next";
import Link from "next/link";
import {
    getAllProblems,
    getPreviousNext,
    getProblemBySlug,
    parsePythonFile,
} from "@/lib/parsePracticeStructure";
import { renderMarkdown } from "@/lib/renderMarkdown";
import CodeBlock from "@/app/components/CodeBlock";
import MarkComplete from "@/app/components/MarkComplete";

// ─── Static Generation ─────────────────────────────────────────────────────

export async function generateStaticParams() {
    const problems = getAllProblems();
    return problems.map((p) => ({
        month: String(p.month),
        week: String(p.week),
        slug: p.slug,
    }));
}

// ─── Dynamic Metadata ──────────────────────────────────────────────────────

type PageProps = {
    params: Promise<{ month: string; week: string; slug: string }>;
};

export async function generateMetadata({
    params,
}: PageProps): Promise<Metadata> {
    const { slug } = await params;
    const problem = getProblemBySlug(slug);
    if (!problem) return { title: "Not Found" };

    const sections = parsePythonFile(problem.filePath);
    const description =
        sections.problemStatement?.slice(0, 155) ||
        `Day ${problem.day} — ${problem.title}. A structured DSA problem with intuition, approach, complexity analysis, and Python code.`;

    return {
        title: problem.title,
        description,
        keywords: [
            problem.title,
            "DSA",
            "data structures",
            "algorithms",
            `week ${problem.week}`,
            "coding problem",
            "Python",
            "interview prep",
        ],
        alternates: {
            canonical: problem.href,
        },
        openGraph: {
            title: `${problem.title} | Algorithm Logbook`,
            description,
            type: "article",
            url: problem.href,
        },
        twitter: {
            card: "summary",
            title: `${problem.title} | Algorithm Logbook`,
            description,
        },
    };
}

// ─── Page Component ────────────────────────────────────────────────────────

export default async function ProblemPage({ params }: PageProps) {
    const { slug } = await params;
    const problem = getProblemBySlug(slug);

    if (!problem) {
        return (
            <div className="text-center py-20">
                <h1 className="text-2xl font-bold mb-2">Problem Not Found</h1>
                <p className="text-muted mb-4">
                    The requested problem does not exist.
                </p>
                <Link href="/" className="text-accent hover:underline">
                    ← Back to Home
                </Link>
            </div>
        );
    }

    const sections = parsePythonFile(problem.filePath);
    const { previous, next } = getPreviousNext(slug);

    // Render all text sections through Markdown + LaTeX pipeline in parallel
    const [
        problemStatementHtml,
        intuitionHtml,
        approachHtml,
        timeComplexityHtml,
        spaceComplexityHtml,
        commonMistakesHtml,
        finalThoughtsHtml,
        codeExplanationHtml,
        patternHtml,
    ] = await Promise.all([
        renderMarkdown(sections.problemStatement),
        renderMarkdown(sections.intuition),
        renderMarkdown(sections.approach),
        renderMarkdown(sections.timeComplexity),
        renderMarkdown(sections.spaceComplexity),
        renderMarkdown(sections.commonMistakes),
        renderMarkdown(sections.finalThoughts),
        renderMarkdown(sections.codeExplanation),
        renderMarkdown(sections.pattern),
    ]);

    // JSON-LD Structured Data
    const siteUrl = "https://algo.ppradosh.com";
    const jsonLd = [
        {
            "@context": "https://schema.org",
            "@type": "LearningResource",
            name: problem.title,
            description:
                sections.problemStatement || `DSA Problem: ${problem.title}`,
            educationalLevel: "Beginner",
            learningResourceType: "Problem",
            inLanguage: "en",
            isAccessibleForFree: true,
            url: `${siteUrl}${problem.href}`,
            provider: {
                "@type": "Organization",
                name: "Algorithm Logbook",
                url: siteUrl,
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            itemListElement: [
                { "@type": "ListItem", position: 1, name: "Home", item: siteUrl },
                {
                    "@type": "ListItem",
                    position: 2,
                    name: `Month ${problem.month}`,
                    item: `${siteUrl}/#month-${problem.month}`,
                },
                {
                    "@type": "ListItem",
                    position: 3,
                    name: `Week ${problem.week}`,
                    item: `${siteUrl}/#month-${problem.month}-week-${problem.week}`,
                },
                {
                    "@type": "ListItem",
                    position: 4,
                    name: problem.title,
                    item: `${siteUrl}${problem.href}`,
                },
            ],
        },
    ];

    return (
        <>
            <script
                type="application/ld+json"
                dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
            />

            <article className="pb-12">
                {/* Breadcrumb */}
                <nav aria-label="Breadcrumb" className="mb-6">
                    <ol className="flex items-center gap-1.5 text-sm text-muted">
                        <li>
                            <Link href="/" className="hover:text-accent transition-colors">
                                Home
                            </Link>
                        </li>
                        <li>
                            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="9 18 15 12 9 6" /></svg>
                        </li>
                        <li>Month {problem.month}</li>
                        <li>
                            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="9 18 15 12 9 6" /></svg>
                        </li>
                        <li>Week {problem.week}</li>
                        <li>
                            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="9 18 15 12 9 6" /></svg>
                        </li>
                        <li className="text-foreground font-medium">Day {problem.day}</li>
                    </ol>
                </nav>

                {/* Header */}
                <header className="mb-8">
                    <div className="flex items-start justify-between gap-4 mb-4">
                        <h1 className="text-2xl font-bold tracking-tight">
                            {problem.title}
                        </h1>
                        <MarkComplete slug={problem.slug} />
                    </div>
                    <div className="flex items-center gap-2 text-sm text-muted">
                        {patternHtml && (
                            <span className="flex items-center gap-2 px-2 py-0.5 rounded-md bg-accent/10 text-accent font-semibold border border-accent/20">
                                <span className="w-2 h-2 rounded-full bg-accent animate-pulse shrink-0" />
                                <span>{patternHtml.replace(/<[^>]*>/g, '').trim()}</span>
                            </span>
                        )}
                    </div>
                </header>

                {/* Content Sections */}
                <div className="space-y-8">
                    {problemStatementHtml && (
                        <ContentSection
                            icon="📋"
                            title="Problem Statement"
                            html={problemStatementHtml}
                        />
                    )}

                    {intuitionHtml && (
                        <ContentSection
                            icon="💡"
                            title="Intuition"
                            html={intuitionHtml}
                        />
                    )}

                    {approachHtml && (
                        <ContentSection
                            icon="🔧"
                            title="Approach"
                            html={approachHtml}
                        />
                    )}

                    {(timeComplexityHtml || spaceComplexityHtml) && (
                        <section className="rounded-xl border border-card-border bg-card p-6">
                            <h2 className="text-base font-semibold mb-4 flex items-center gap-2">
                                <span>⚡</span> Complexity Analysis
                            </h2>
                            <div className="grid grid-cols-2 gap-4">
                                {timeComplexityHtml && (
                                    <div className="p-3 rounded-lg bg-muted-bg">
                                        <div className="text-xs text-muted uppercase tracking-wider mb-2">
                                            Time
                                        </div>
                                        <div
                                            className="text-sm font-medium [&_.katex]:text-foreground [&_p]:m-0"
                                            dangerouslySetInnerHTML={{ __html: timeComplexityHtml }}
                                        />
                                    </div>
                                )}
                                {spaceComplexityHtml && (
                                    <div className="p-3 rounded-lg bg-muted-bg">
                                        <div className="text-xs text-muted uppercase tracking-wider mb-2">
                                            Space
                                        </div>
                                        <div
                                            className="text-sm font-medium [&_.katex]:text-foreground [&_p]:m-0"
                                            dangerouslySetInnerHTML={{ __html: spaceComplexityHtml }}
                                        />
                                    </div>
                                )}
                            </div>
                        </section>
                    )}

                    {commonMistakesHtml && (
                        <ContentSection
                            icon="⚠️"
                            title="Common Mistakes"
                            html={commonMistakesHtml}
                        />
                    )}

                    {finalThoughtsHtml && (
                        <ContentSection
                            icon="🎯"
                            title="Final Thoughts"
                            html={finalThoughtsHtml}
                        />
                    )}

                    {/* Code Section */}
                    {sections.code && (
                        <section>
                            <CodeBlock
                                code={sections.code}
                                explanationHtml={codeExplanationHtml || undefined}
                            />
                        </section>
                    )}
                </div>

                {/* Previous / Next */}
                <nav
                    aria-label="Problem navigation"
                    className="mt-12 pt-8 border-t border-card-border"
                >
                    <div className="flex justify-between gap-3">
                        {previous ? (
                            <Link
                                href={previous.href}
                                className="group flex-1 min-w-0 flex items-center gap-2 px-3 py-3 rounded-xl border border-card-border bg-card hover:border-accent/40 hover:shadow-[var(--shadow)] transition-all duration-200"
                            >
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-muted group-hover:text-accent transition-colors shrink-0"><polyline points="15 18 9 12 15 6" /></svg>
                                <div className="min-w-0 overflow-hidden">
                                    <div className="text-xs text-muted">Previous</div>
                                    <div className="text-sm font-medium truncate group-hover:text-accent transition-colors">
                                        {previous.title}
                                    </div>
                                </div>
                            </Link>
                        ) : (
                            <div className="flex-1" />
                        )}

                        {next ? (
                            <Link
                                href={next.href}
                                className="group flex-1 min-w-0 flex items-center justify-end gap-2 px-3 py-3 rounded-xl border border-card-border bg-card hover:border-accent/40 hover:shadow-[var(--shadow)] transition-all duration-200 text-right"
                            >
                                <div className="min-w-0 overflow-hidden">
                                    <div className="text-xs text-muted">Next</div>
                                    <div className="text-sm font-medium truncate group-hover:text-accent transition-colors">
                                        {next.title}
                                    </div>
                                </div>
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-muted group-hover:text-accent transition-colors shrink-0"><polyline points="9 18 15 12 9 6" /></svg>
                            </Link>
                        ) : (
                            <div className="flex-1" />
                        )}
                    </div>
                </nav>

                {/* GitHub Issues */}
                <div className="mt-8 pt-6 border-t border-card-border flex justify-center">
                    <a
                        href="https://github.com/prpigitcse/dsa-daily-practice/issues"
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-1.5 text-xs text-muted hover:text-accent transition-colors duration-200"
                    >
                        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <circle cx="12" cy="12" r="10" />
                            <line x1="12" y1="8" x2="12" y2="12" />
                            <line x1="12" y1="16" x2="12.01" y2="16" />
                        </svg>
                        Report an issue or suggest an improvement
                    </a>
                </div>
            </article>
        </>
    );
}

// ─── Reusable Content Section ──────────────────────────────────────────────

function ContentSection({
    icon,
    title,
    html,
}: {
    icon: string;
    title: string;
    html: string;
}) {
    return (
        <section className="rounded-xl border border-card-border bg-card p-6">
            <h2 className="text-base font-semibold mb-3 flex items-center gap-2">
                <span>{icon}</span> {title}
            </h2>
            <div
                className="text-sm leading-relaxed text-muted [&_p]:mb-2 [&_p:last-child]:mb-0 [&_ol]:list-decimal [&_ol]:pl-5 [&_ol]:space-y-1 [&_ul]:list-disc [&_ul]:pl-5 [&_ul]:space-y-1 [&_.katex]:text-foreground"
                dangerouslySetInnerHTML={{ __html: html }}
            />
        </section>
    );
}
