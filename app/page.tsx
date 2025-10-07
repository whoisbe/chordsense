export default function Home() {
  return (
    <main className="max-w-2xl mx-auto p-6">
      <h1 className="text-3xl font-bold">Chordsense</h1>
      <p className="mt-4 text-gray-600">
        Learning music theory while building tools with DuckDB + Next.js.
      </p>
      <ul className="mt-6 space-y-2">
        <li>
          <a href="/blog" className="underline">Read the Blog</a>
        </li>
      </ul>
    </main>
  );
}
