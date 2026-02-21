"use client";

import { useEffect, useRef, useState } from "react";
import hljs from "highlight.js/lib/core";
import python from "highlight.js/lib/languages/python";
import "highlight.js/styles/atom-one-dark.css";

hljs.registerLanguage("python", python);

interface CodeBlockProps {
    code: string;
    explanation?: string;
}

export default function CodeBlock({ code, explanation }: CodeBlockProps) {
    const [showCode, setShowCode] = useState(false);
    const [showExplain, setShowExplain] = useState(false);
    const codeRef = useRef<HTMLElement>(null);

    useEffect(() => {
        if (showCode && codeRef.current) {
            hljs.highlightElement(codeRef.current);
        }
    }, [showCode, code]);

    return (
        <div className="mt-6">
            <button
                onClick={() => setShowCode(!showCode)}
                className="inline-flex items-center gap-2 px-4 py-2.5 rounded-lg text-sm font-medium bg-card border border-card-border hover:bg-nav-hover transition-all duration-200 cursor-pointer"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                >
                    <polyline points="16 18 22 12 16 6" />
                    <polyline points="8 6 2 12 8 18" />
                </svg>
                {showCode ? "Hide Code" : "View Code"}
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
                    className={`transition-transform duration-200 ${showCode ? "rotate-180" : ""}`}
                >
                    <polyline points="6 9 12 15 18 9" />
                </svg>
            </button>

            {showCode && (
                <div className="mt-3 animate-in fade-in slide-in-from-top-2 duration-300">
                    <pre className="rounded-xl overflow-hidden shadow-lg">
                        <code ref={codeRef} className="language-python">
                            {code}
                        </code>
                    </pre>

                    {explanation && (
                        <div className="mt-3">
                            <button
                                onClick={() => setShowExplain(!showExplain)}
                                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-medium text-muted hover:text-foreground hover:bg-nav-hover transition-all duration-200 cursor-pointer"
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
                                    <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
                                    <line x1="12" y1="17" x2="12.01" y2="17" />
                                </svg>
                                {showExplain ? "Hide Explanation" : "Explain Code"}
                            </button>

                            {showExplain && (
                                <div className="mt-2 p-4 rounded-lg bg-muted-bg border border-card-border text-sm leading-relaxed whitespace-pre-wrap">
                                    {explanation}
                                </div>
                            )}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}
