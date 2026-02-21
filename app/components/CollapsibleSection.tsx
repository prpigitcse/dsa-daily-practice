"use client";

import { useState } from "react";

export function CollapsibleMonth({
    monthNumber,
    defaultOpen = true,
    children,
}: {
    monthNumber: number;
    defaultOpen?: boolean;
    children: React.ReactNode;
}) {
    const [open, setOpen] = useState(defaultOpen);

    return (
        <div className="mb-8">
            <button
                onClick={() => setOpen(!open)}
                className="w-full flex items-center gap-2 text-lg font-semibold group cursor-pointer"
                aria-expanded={open}
            >
                <span className="w-7 h-7 rounded-lg bg-accent-bg text-accent text-xs font-bold flex items-center justify-center">
                    {monthNumber}
                </span>
                <span className="flex-1 text-left">Month {monthNumber}</span>
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
                    className={`text-muted transition-transform duration-200 ${open ? "rotate-180" : ""}`}
                >
                    <polyline points="6 9 12 15 18 9" />
                </svg>
            </button>

            <div
                className={`grid transition-all duration-300 ease-in-out ${open ? "grid-rows-[1fr] opacity-100 mt-4" : "grid-rows-[0fr] opacity-0 mt-0"}`}
            >
                <div className="overflow-hidden">
                    <div className="space-y-4 pl-2">{children}</div>
                </div>
            </div>
        </div>
    );
}

export function CollapsibleWeek({
    weekNumber,
    defaultOpen = true,
    children,
}: {
    weekNumber: number;
    defaultOpen?: boolean;
    children: React.ReactNode;
}) {
    const [open, setOpen] = useState(defaultOpen);

    return (
        <div>
            <button
                onClick={() => setOpen(!open)}
                className="w-full flex items-center gap-2 mb-2 cursor-pointer group"
                aria-expanded={open}
            >
                <h3 className="text-sm font-medium text-muted uppercase tracking-wider group-hover:text-foreground transition-colors duration-150">
                    Week {weekNumber}
                </h3>
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="12"
                    height="12"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    className={`text-muted transition-transform duration-200 ${open ? "rotate-180" : ""}`}
                >
                    <polyline points="6 9 12 15 18 9" />
                </svg>
            </button>

            <div
                className={`grid transition-all duration-300 ease-in-out ${open ? "grid-rows-[1fr] opacity-100" : "grid-rows-[0fr] opacity-0"}`}
            >
                <div className="overflow-hidden">
                    {children}
                </div>
            </div>
        </div>
    );
}
