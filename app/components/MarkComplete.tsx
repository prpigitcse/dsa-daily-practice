"use client";

import { useEffect, useState } from "react";

interface MarkCompleteProps {
    slug: string;
}

function getCompleted(): string[] {
    if (typeof window === "undefined") return [];
    try {
        return JSON.parse(localStorage.getItem("dsa-completed") || "[]");
    } catch {
        return [];
    }
}

function setCompleted(slugs: string[]) {
    localStorage.setItem("dsa-completed", JSON.stringify(slugs));
}

export default function MarkComplete({ slug }: MarkCompleteProps) {
    const [completed, setIsCompleted] = useState(false);
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
        const list = getCompleted();
        setIsCompleted(list.includes(slug));
    }, [slug]);

    const toggle = () => {
        const list = getCompleted();
        if (list.includes(slug)) {
            setCompleted(list.filter((s) => s !== slug));
            setIsCompleted(false);
        } else {
            setCompleted([...list, slug]);
            setIsCompleted(true);
        }
    };

    if (!mounted) return <div className="h-10" />;

    return (
        <button
            onClick={toggle}
            className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 cursor-pointer ${completed
                    ? "bg-success-bg text-success border border-success/30"
                    : "bg-accent-bg text-accent border border-accent/30 hover:bg-accent hover:text-white"
                }`}
        >
            {completed ? (
                <>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><polyline points="20 6 9 17 4 12" /></svg>
                    Completed ✓
                </>
            ) : (
                <>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10" /></svg>
                    Mark as Completed
                </>
            )}
        </button>
    );
}
