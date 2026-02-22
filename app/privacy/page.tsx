import type { Metadata } from "next";

export const metadata: Metadata = {
    title: "Privacy Policy",
    description:
        "Privacy policy for Algorithm Logbook. Learn how we handle data and analytics on this site.",
    alternates: {
        canonical: "/privacy",
    },
    robots: {
        index: true,
        follow: true,
    },
};

export default function PrivacyPage() {
    return (
        <article className="max-w-2xl space-y-5 leading-relaxed">
            <h1 className="text-2xl font-bold tracking-tight mb-1">Privacy Policy</h1>
            <p className="text-muted text-sm">Last updated: February 2026</p>

            <p>
                This website does not collect personal information directly.
            </p>

            <p>
                We use{" "}
                <a
                    href="https://vercel.com/analytics"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-accent hover:underline"
                >
                    Vercel Analytics
                </a>{" "}
                to understand general usage patterns such as page views and referrer
                data. Vercel Analytics does not use cookies for tracking and does not
                collect personally identifiable information.
            </p>

            <p>
                We also use{" "}
                <a
                    href="https://vercel.com/docs/speed-insights"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-accent hover:underline"
                >
                    Vercel Speed Insights
                </a>{" "}
                to measure real-world performance metrics (Core Web Vitals) such as page
                load times and interaction responsiveness. This data is aggregated and
                anonymous — no personal information or cookies are involved.
            </p>

            <p>
                No user accounts, forms, or email subscriptions are currently
                implemented.
            </p>

            <p>
                If this changes in the future, this policy will be updated accordingly.
            </p>
        </article>
    );
}
