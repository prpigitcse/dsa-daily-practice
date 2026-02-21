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

export const metadata: Metadata = {
  title: {
    default: "DSA Daily Practice",
    template: "%s | DSA Daily Practice",
  },
  description:
    "Learn Data Structures & Algorithms through daily practice. A structured, consistency-driven approach to mastering DSA concepts.",
  openGraph: {
    title: "DSA Daily Practice",
    description:
      "Learn Data Structures & Algorithms through daily practice.",
    type: "website",
    siteName: "DSA Daily Practice",
  },
  twitter: {
    card: "summary",
    title: "DSA Daily Practice",
    description:
      "Learn Data Structures & Algorithms through daily practice.",
  },
  robots: {
    index: true,
    follow: true,
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
              DSA Daily Practice
            </a>
            <ThemeToggle />
          </div>
        </header>
        <main className="max-w-3xl mx-auto px-6 py-8">{children}</main>
        <footer className="border-t border-card-border mt-16">
          <div className="max-w-3xl mx-auto px-6 py-6 text-center text-xs text-muted">
            Built with consistency · DSA Daily Practice
          </div>
        </footer>
      </body>
    </html>
  );
}
