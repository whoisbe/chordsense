import fs from "node:fs/promises";
import path from "node:path";
import matter from "gray-matter";
import { MDXRemote } from "next-mdx-remote/rsc";

const POSTS_DIR = path.join(process.cwd(), "content");

export default async function PostPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const filePath = path.join(POSTS_DIR, `${slug}.mdx`);
  const file = await fs.readFile(filePath, "utf8");
  const { content, data } = matter(file);

  return (
    <main className="prose prose-gray max-w-2xl mx-auto p-6">
      <h1 className="text-3xl font-bold">{data.title}</h1>
      <p className="text-gray-500 text-sm">{data.date}</p>
      <article className="mt-6">
        <MDXRemote source={content} />
      </article>
    </main>
  );
}
