import fs from "node:fs/promises";
import path from "node:path";
import matter from "gray-matter";
import Link from "next/link";

const POSTS_DIR = path.join(process.cwd(), "content");

interface PostMeta {
  slug: string;
  title: string;
  summary: string;
  date: string;
}

export default async function BlogIndex() {
  const files = await fs.readdir(POSTS_DIR);
  const posts: PostMeta[] = await Promise.all(
    files.map(async (file) => {
      const raw = await fs.readFile(path.join(POSTS_DIR, file), "utf8");
      const { data } = matter(raw);
      return { 
        slug: file.replace(".mdx", ""), 
        title: data.title as string,
        summary: data.summary as string,
        date: data.date as string,
      };
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
