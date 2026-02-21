import Link from "next/link";
import { parsePracticeStructure, flattenProblems } from "@/lib/parsePracticeStructure";
import { CompletionBadge, CompletionCount } from "./components/CompletionTracker";
import { CollapsibleMonth, CollapsibleWeek } from "./components/CollapsibleSection";
import { DailyQuote } from "./components/DailyQuote";

export default function Home() {
  const tree = parsePracticeStructure();
  const allProblems = flattenProblems();
  const totalCount = allProblems.length;

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify([
            {
              "@context": "https://schema.org",
              "@type": "WebSite",
              name: "Algorithm Logbook",
              url: "https://dsa-daily-practice.vercel.app",
              description:
                "Master Data Structures & Algorithms one problem at a time. A free, structured, consistency-driven learning platform.",
            },
            {
              "@context": "https://schema.org",
              "@type": "ItemList",
              name: "DSA Problems",
              numberOfItems: totalCount,
              itemListElement: allProblems.slice(0, 10).map((p, i) => ({
                "@type": "ListItem",
                position: i + 1,
                name: p.title,
                url: `https://dsa-daily-practice.vercel.app${p.href}`,
              })),
            },
          ]),
        }}
      />
      <article>
        {/* Hero */}
        <section className="mb-10">
          <h1 className="text-3xl font-bold tracking-tight mb-2">
            Algorithm Logbook
          </h1>
          <p className="text-muted text-base leading-relaxed mb-6">
            One problem a day. One concept at a time.<br />
            Your daily grind toward algorithmic mastery.
          </p>

          <DailyQuote />

          <div className="flex items-center gap-4 mb-4 mt-6">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-accent-bg text-accent text-sm font-medium">
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" /><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" /></svg>
              {totalCount} Problems
            </span>
          </div>

          <CompletionCount total={totalCount} />
        </section>

        {/* Hierarchy */}
        <section>
          {tree.map((month) => (
            <CollapsibleMonth key={month.month} monthNumber={month.month}>
              {month.weeks.map((week) => (
                <CollapsibleWeek key={week.week} weekNumber={week.week}>
                  <div className="grid gap-1.5">
                    {week.problems.map((problem) => (
                      <Link
                        key={problem.slug}
                        href={problem.href}
                        className="group flex items-center gap-3 px-4 py-3 rounded-xl border border-card-border bg-card hover:border-accent/40 hover:shadow-[var(--shadow)] transition-all duration-200"
                      >
                        <span className="w-8 h-8 rounded-lg bg-muted-bg group-hover:bg-accent-bg text-muted group-hover:text-accent text-xs font-bold flex items-center justify-center shrink-0 transition-colors duration-200">
                          {problem.day}
                        </span>
                        <span className="flex-1 text-sm font-medium group-hover:text-accent transition-colors duration-200">
                          {problem.title}
                        </span>
                        <CompletionBadge slug={problem.slug} />
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-muted/40 group-hover:text-accent transition-all duration-200 group-hover:translate-x-0.5"><polyline points="9 18 15 12 9 6" /></svg>
                      </Link>
                    ))}
                  </div>
                </CollapsibleWeek>
              ))}
            </CollapsibleMonth>
          ))}
        </section>
      </article>
    </>
  );
}
