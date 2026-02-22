import type { Metadata } from "next";
import Link from "next/link";
import { parsePracticeStructure } from "@/lib/parsePracticeStructure";

export const metadata: Metadata = {
    title: "Sitemap",
    description: "A complete list of all problems and pages on Algorithm Logbook.",
    alternates: {
        canonical: "/sitemap",
    },
    robots: {
        index: true,
        follow: true,
    },
};

export default function SitemapPage() {
    const tree = parsePracticeStructure();

    return (
        <article className="max-w-2xl">
            <h1 className="text-2xl font-bold tracking-tight mb-1">Sitemap</h1>
            <p className="text-muted text-sm mb-8">All pages and problems on Algorithm Logbook.</p>

            {/* Static pages */}
            <section className="mb-8">
                <h2 className="text-xs font-semibold uppercase tracking-widest text-muted mb-3">Pages</h2>
                <ul className="space-y-1">
                    {[
                        { label: "Home", href: "/" },
                        { label: "Privacy Policy", href: "/privacy" },
                        { label: "Sitemap", href: "/sitemap" },
                    ].map(({ label, href }) => (
                        <li key={href}>
                            <Link
                                href={href}
                                className="flex items-center gap-2 text-sm py-1.5 text-accent hover:underline underline-offset-4"
                            >
                                <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="shrink-0 opacity-60"><path d="M15 3h6v6" /><path d="M10 14 21 3" /><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" /></svg>
                                {label}
                            </Link>
                        </li>
                    ))}
                </ul>
            </section>

            {/* Problems grouped by month → week */}
            {tree.map((month) => (
                <section key={month.month} className="mb-8">
                    <h2 className="text-xs font-semibold uppercase tracking-widest text-muted mb-3">
                        Month {month.month}
                    </h2>

                    {month.weeks.map((week) => (
                        <div key={week.week} className="mb-5">
                            <h3 className="text-sm font-semibold mb-2 text-foreground/70">Week {week.week}</h3>
                            <ul className="space-y-1 pl-2 border-l border-card-border">
                                {week.problems.map((problem) => (
                                    <li key={problem.slug}>
                                        <Link
                                            href={problem.href}
                                            className="flex items-center gap-2 text-sm py-1 pl-3 text-accent hover:underline underline-offset-4"
                                        >
                                            <span className="text-muted text-xs font-mono shrink-0">
                                                Day {problem.day}
                                            </span>
                                            {problem.title}
                                        </Link>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    ))}
                </section>
            ))}
        </article>
    );
}
