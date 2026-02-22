import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
    title: "404 — Page Not Found",
    description: "The page you're looking for doesn't exist.",
    robots: { index: false, follow: false },
};

export default function NotFound() {
    return (
        <div className="min-h-[70vh] flex flex-col items-center justify-center text-center px-6 select-none">

            {/* Big 404 */}
            <div className="relative mb-6">
                <span
                    className="text-[9rem] sm:text-[12rem] font-black leading-none tracking-tighter text-transparent"
                    style={{
                        WebkitTextStroke: "2px var(--card-border)",
                    }}
                >
                    404
                </span>
                {/* Glowing accent overlay */}
                <span
                    className="absolute inset-0 flex items-center justify-center text-[9rem] sm:text-[12rem] font-black leading-none tracking-tighter text-transparent"
                    style={{
                        WebkitTextStroke: "2px var(--accent)",
                        clipPath: "inset(0 60% 0 0)",
                        opacity: 0.6,
                    }}
                    aria-hidden="true"
                >
                    404
                </span>
            </div>

            {/* Code-flavoured badge */}
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border border-card-border bg-card text-xs font-mono text-muted mb-5">
                <span className="w-2 h-2 rounded-full bg-accent animate-pulse shrink-0" />
                <span>
                    <span className="text-accent">TypeError</span>
                    {": "}
                    Cannot read properties of{" "}
                    <span className="text-accent">undefined</span>
                    {" (reading 'page')"}
                </span>
            </div>

            <h1 className="text-2xl font-bold tracking-tight mb-2">
                Page not found
            </h1>
            <p className="text-muted text-sm max-w-xs mb-8 leading-relaxed">
                This URL doesn&apos;t map to any known route. It may have moved,
                been deleted, or never existed.
            </p>

            {/* Actions */}
            <div className="flex items-center gap-3 flex-wrap justify-center">
                <Link
                    href="/"
                    className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-accent text-white text-sm font-medium hover:opacity-90 transition-opacity duration-200"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="14"
                        height="14"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                    >
                        <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
                        <polyline points="9 22 9 12 15 12 15 22" />
                    </svg>
                    Back to Home
                </Link>
                <a
                    href="https://github.com/prpigitcse/dsa-daily-practice/issues"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 px-4 py-2 rounded-xl border border-card-border bg-card text-sm font-medium text-muted hover:text-accent hover:border-accent/40 transition-all duration-200"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="14"
                        height="14"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                    >
                        <circle cx="12" cy="12" r="10" />
                        <line x1="12" y1="8" x2="12" y2="12" />
                        <line x1="12" y1="16" x2="12.01" y2="16" />
                    </svg>
                    Report an issue
                </a>
            </div>
        </div>
    );
}
