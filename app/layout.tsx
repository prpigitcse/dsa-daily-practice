import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import ThemeToggle from "./components/ThemeToggle";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const siteUrl = "https://dsa-daily-practice.vercel.app";

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: "DSA Logbook — Daily Data Structures & Algorithms Practice",
    template: "%s | DSA Logbook",
  },
  description:
    "Master Data Structures & Algorithms one problem at a time. DSA Logbook is a free, structured, consistency-driven learning platform with 22+ problems covering arrays, recursion, sorting, searching, number theory, and more.",
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
  authors: [{ name: "DSA Logbook" }],
  creator: "DSA Logbook",
  publisher: "DSA Logbook",
  category: "Education",
  alternates: {
    canonical: "/",
  },
  openGraph: {
    title: "DSA Logbook — Daily Data Structures & Algorithms Practice",
    description:
      "Master DSA one problem at a time. Free, structured, consistency-driven learning with 22+ problems across arrays, recursion, sorting, and more.",
    type: "website",
    siteName: "DSA Logbook",
    url: "/",
    locale: "en_US",
  },
  twitter: {
    card: "summary_large_image",
    title: "DSA Logbook — Daily DSA Practice",
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
              className="text-sm font-semibold tracking-tight hover:text-accent transition-colors"
            >
              DSA Logbook
            </a>
            <ThemeToggle />
          </div>
        </header>
        <main className="max-w-3xl mx-auto px-6 py-8">{children}</main>
        <footer className="border-t border-card-border mt-16">
          <div className="max-w-3xl mx-auto px-6 py-6 text-center text-xs text-muted">
            Built with consistency · DSA Logbook
          </div>
        </footer>
      </body>
    </html>
  );
}
