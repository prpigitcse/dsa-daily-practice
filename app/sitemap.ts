import type { MetadataRoute } from "next";
import { getAllProblems } from "@/lib/parsePracticeStructure";

export default function sitemap(): MetadataRoute.Sitemap {
    const problems = getAllProblems();
    const baseUrl = "https://dsa-daily-practice.vercel.app";

    const problemUrls: MetadataRoute.Sitemap = problems.map((p) => ({
        url: `${baseUrl}${p.href}`,
        lastModified: new Date(),
        changeFrequency: "weekly" as const,
        priority: 0.8,
    }));

    return [
        {
            url: baseUrl,
            lastModified: new Date(),
            changeFrequency: "daily",
            priority: 1.0,
        },
        ...problemUrls,
    ];
}
