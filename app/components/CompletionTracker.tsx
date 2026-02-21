"use client";

import { useEffect, useState } from "react";

interface CompletionBadgeProps {
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

export function CompletionBadge({ slug }: CompletionBadgeProps) {
    const [completed, setCompleted] = useState(false);

    useEffect(() => {
        setCompleted(getCompleted().includes(slug));
    }, [slug]);

    if (!completed) return null;

    return (
        <span
            className="inline-flex items-center justify-center w-5 h-5 rounded-full bg-success-bg text-success text-xs"
            title="Completed"
        >
            ✓
        </span>
    );
}

interface CompletionCountProps {
    total: number;
}

export function CompletionCount({ total }: CompletionCountProps) {
    const [count, setCount] = useState(0);
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
        setCount(getCompleted().length);
    }, []);

    if (!mounted) return null;

    const percent = total > 0 ? Math.round((count / total) * 100) : 0;

    return (
        <div className="flex items-center gap-3">
            <div className="flex-1 h-2 rounded-full bg-muted-bg overflow-hidden">
                <div
                    className="h-full rounded-full bg-accent transition-all duration-500 ease-out"
                    style={{ width: `${percent}%` }}
                />
            </div>
            <span className="text-sm font-medium text-muted whitespace-nowrap">
                {count}/{total} completed
            </span>
        </div>
    );
}
