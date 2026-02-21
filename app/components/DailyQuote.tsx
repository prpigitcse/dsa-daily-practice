"use client";

import { useState, useEffect } from "react";

const quotes = [
    { text: "First, solve the problem. Then, write the code.", author: "John Johnson" },
    { text: "The only way to learn a new programming language is by writing programs in it.", author: "Dennis Ritchie" },
    { text: "It's not that I'm so smart, it's just that I stay with problems longer.", author: "Albert Einstein" },
    { text: "Simplicity is the soul of efficiency.", author: "Austin Freeman" },
    { text: "Talk is cheap. Show me the code.", author: "Linus Torvalds" },
    { text: "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", author: "Martin Fowler" },
    { text: "The best time to plant a tree was 20 years ago. The second best time is now.", author: "Chinese Proverb" },
    { text: "Programs must be written for people to read, and only incidentally for machines to execute.", author: "Harold Abelson" },
    { text: "The most damaging phrase in the language is: 'We've always done it this way.'", author: "Grace Hopper" },
    { text: "Consistency is more important than intensity.", author: "Unknown" },
    { text: "Big things are built one brick at a time.", author: "Unknown" },
    { text: "An algorithm must be seen to be believed.", author: "Donald Knuth" },
    { text: "Weeks of coding can save you hours of planning.", author: "Unknown" },
    { text: "Every expert was once a beginner.", author: "Helen Hayes" },
    { text: "The function of good software is to make the complex appear to be simple.", author: "Grady Booch" },
    { text: "Don't worry about what anybody else is going to do. The best way to predict the future is to invent it.", author: "Alan Kay" },
    { text: "Debugging is twice as hard as writing the code in the first place.", author: "Brian Kernighan" },
    { text: "Small daily improvements over time lead to stunning results.", author: "Robin Sharma" },
    { text: "The hardest part of design is keeping features out.", author: "Donald Norman" },
    { text: "What one programmer can do in one month, two programmers can do in two months.", author: "Fred Brooks" },
    { text: "Discipline is choosing between what you want now and what you want most.", author: "Abraham Lincoln" },
    { text: "You don't have to be great to start, but you have to start to be great.", author: "Zig Ziglar" },
    { text: "Computer science is no more about computers than astronomy is about telescopes.", author: "Edsger Dijkstra" },
    { text: "Before software can be reusable it first has to be usable.", author: "Ralph Johnson" },
    { text: "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away.", author: "Antoine de Saint-Exupéry" },
    { text: "Learning never exhausts the mind.", author: "Leonardo da Vinci" },
    { text: "The secret of getting ahead is getting started.", author: "Mark Twain" },
    { text: "We are what we repeatedly do. Excellence is not an act, but a habit.", author: "Aristotle" },
    { text: "Knowing is not enough; we must apply. Willing is not enough; we must do.", author: "Johann Wolfgang von Goethe" },
    { text: "A person who never made a mistake never tried anything new.", author: "Albert Einstein" },
];

export function DailyQuote() {
    const [quote, setQuote] = useState<typeof quotes[0] | null>(null);

    useEffect(() => {
        const today = new Date();
        const seed = today.getFullYear() * 10000 + (today.getMonth() + 1) * 100 + today.getDate();
        const index = seed % quotes.length;
        setQuote(quotes[index]);
    }, []);

    if (!quote) return null;

    return (
        <div className="flex gap-3 px-4 py-3 rounded-lg border-l-4 border-l-accent bg-accent-bg/40">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-accent shrink-0 mt-0.5">
                <path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5" />
                <path d="M9 18h6" />
                <path d="M10 22h4" />
            </svg>
            <div>
                <p className="text-sm text-foreground leading-relaxed">{quote.text}</p>
                <p className="text-xs text-muted mt-1">— {quote.author}</p>
            </div>
        </div>
    );
}
