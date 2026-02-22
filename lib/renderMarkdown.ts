import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkMath from "remark-math";
import remarkRehype from "remark-rehype";
import rehypeKatex from "rehype-katex";
import rehypeStringify from "rehype-stringify";

/**
 * Convert a markdown string (with optional LaTeX math) to an HTML string.
 * Inline math: $...$   Block math: $$...$$
 */
export async function renderMarkdown(source: string): Promise<string> {
    if (!source) return "";
    const result = await unified()
        .use(remarkParse)
        .use(remarkMath)
        .use(remarkRehype)
        .use(rehypeKatex)
        .use(rehypeStringify)
        .process(source);
    return String(result);
}
