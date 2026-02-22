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

          <div className="flex items-center gap-3 mt-5 mb-5 flex-wrap">
            <a
              href="https://github.com/prpigitcse/dsa-daily-practice"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-card-border bg-card hover:border-accent/40 hover:text-accent text-xs font-medium text-muted transition-all duration-200"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23A11.51 11.51 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.29-1.552 3.297-1.23 3.297-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 21.795 24 17.295 24 12c0-6.63-5.37-12-12-12" />
              </svg>
              GitHub
            </a>
            <a
              href="https://github.com/prpigitcse/dsa-daily-practice/issues"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-card-border bg-card hover:border-accent/40 hover:text-accent text-xs font-medium text-muted transition-all duration-200"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="10" />
                <line x1="12" y1="8" x2="12" y2="12" />
                <line x1="12" y1="16" x2="12.01" y2="16" />
              </svg>
              Issues
            </a>
            <a
              href="https://github.com/prpigitcse/dsa-daily-practice/discussions"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-card-border bg-card hover:border-accent/40 hover:text-accent text-xs font-medium text-muted transition-all duration-200"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
              </svg>
              Discussions
            </a>
          </div>

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
