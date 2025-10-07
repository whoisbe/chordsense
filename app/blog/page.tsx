import fs from "node:fs/promises";
import path from "node:path";
import matter from "gray-matter";
import Link from "next/link";

const POSTS_DIR = path.join(process.cwd(), "content");

export default async function BlogIndex() {
  const files = await fs.readdir(POSTS_DIR);
  const posts = await Promise.all(
    files.map(async (file) => {
      const raw = await fs.readFile(path.join(POSTS_DIR, file), "utf8");
      const { data } = matter(raw);
      return { slug: file.replace(".mdx", ""), ...data };
    })
  );

  return (
    <main className="max-w-2xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Blog</h1>
      <ul className="space-y-4">
        {posts.map((post) => (
          <li key={post.slug}>
            <Link href={`/blog/${post.slug}`} className="text-xl font-semibold underline">
              {post.title}
            </Link>
            <p className="text-sm text-gray-500">{post.summary}</p>
          </li>
        ))}
      </ul>
    </main>
  );
}
