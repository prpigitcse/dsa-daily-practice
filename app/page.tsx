import Link from "next/link";
import { parsePracticeStructure, flattenProblems } from "@/lib/parsePracticeStructure";
import { CompletionBadge, CompletionCount } from "./components/CompletionTracker";

export default function Home() {
  const tree = parsePracticeStructure();
  const allProblems = flattenProblems();
  const totalCount = allProblems.length;

  return (
    <article>
      {/* Hero */}
      <section className="mb-10">
        <h1 className="text-3xl font-bold tracking-tight mb-2">
          DSA Daily Practice
        </h1>
        <p className="text-muted text-base leading-relaxed mb-6">
          Learn Data Structures & Algorithms Through Consistency
        </p>

        <div className="flex items-center gap-4 mb-4">
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
          <div key={month.month} className="mb-8">
            <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <span className="w-7 h-7 rounded-lg bg-accent-bg text-accent text-xs font-bold flex items-center justify-center">
                {month.month}
              </span>
              Month {month.month}
            </h2>

            <div className="space-y-4 pl-2">
              {month.weeks.map((week) => (
                <div key={week.week}>
                  <h3 className="text-sm font-medium text-muted mb-2 uppercase tracking-wider">
                    Week {week.week}
                  </h3>
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
                </div>
              ))}
            </div>
          </div>
        ))}
      </section>
    </article>
  );
}
