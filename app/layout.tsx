import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";
import ThemeToggle from "./components/ThemeToggle";
import "katex/dist/katex.min.css";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const siteUrl = "https://algo.ppradosh.com";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: "Algorithm Logbook — Daily Data Structures & Algorithms Practice",
    template: "%s | Algorithm Logbook",
  },
  description:
    "Master Data Structures & Algorithms one problem at a time. Algorithm Logbook is a free, structured, consistency-driven learning platform with 22+ problems covering arrays, recursion, sorting, searching, number theory, and more.",
  keywords: [
    "DSA",
    "data structures",
    "algorithms",
    "coding practice",
    "learn DSA",
    "programming problems",
    "binary search",
    "recursion",
    "sorting algorithms",
    "bubble sort",
    "linear search",
    "time complexity",
    "space complexity",
    "competitive programming",
    "interview preparation",
    "Python DSA",
    "algorithm tutorial",
    "daily coding practice",
  ],
  authors: [{ name: "Pradosh Ranjan Pattanayak" }],
  creator: "Pradosh Ranjan Pattanayak",
  publisher: "Pradosh Ranjan Pattanayak",
  category: "Education",
  alternates: {
    canonical: "/",
  },
  openGraph: {
    title: "Algorithm Logbook — Daily Data Structures & Algorithms Practice",
    description:
      "Master DSA one problem at a time. Free, structured, consistency-driven learning with 22+ problems across arrays, recursion, sorting, and more.",
    type: "website",
    siteName: "Algorithm Logbook",
    url: "/",
    locale: "en_US",
  },
  twitter: {
    card: "summary_large_image",
    title: "Algorithm Logbook — Daily DSA Practice",
    description:
      "Master Data Structures & Algorithms one problem at a time. Free, structured, consistency-driven learning.",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <script
          dangerouslySetInnerHTML={{
            __html: `
              (function() {
                try {
                  var theme = localStorage.getItem('theme');
                  var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                  if (theme === 'dark' || (!theme && prefersDark)) {
                    document.documentElement.classList.add('dark');
                  }
                } catch(e) {}
              })();
            `,
          }}
        />
      </head>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased min-h-screen bg-background text-foreground`}
      >
        <header className="sticky top-0 z-50 backdrop-blur-md bg-background/80 border-b border-card-border">
          <div className="max-w-3xl mx-auto px-6 h-14 flex items-center justify-between">
            <a
              href="/"
              className="flex items-center gap-2 text-sm font-semibold tracking-tight hover:text-accent transition-colors"
            >
              <img src="/logo.svg" alt="Algorithm Logbook" width={28} height={28} />
              Algorithm Logbook
            </a>
            <ThemeToggle />
          </div>
        </header>
        <main className="max-w-3xl mx-auto px-6 py-8">{children}</main>
        <footer className="border-t border-card-border mt-16">
          <div className="max-w-3xl mx-auto px-6 py-6 text-center text-xs text-muted">
            Built with consistency · Algorithm Logbook
            <br />
            © {new Date().getFullYear()} Pradosh. Educational content for personal learning and reference.
            <br />
            <span className="inline-flex items-center gap-2 mt-2">
              <a href="/privacy" className="hover:text-accent transition-colors">
                Privacy Policy
              </a>
              <span aria-hidden="true">·</span>
              <a href="/sitemap" className="hover:text-accent transition-colors">
                Sitemap
              </a>
            </span>
          </div>
        </footer>
        <Analytics />
        <SpeedInsights />
      </body>
    </html>
  );
}
