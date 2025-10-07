import './globals.css'

export const metadata = {
  title: 'Chordsense',
  description: 'Learning music theory while building tools with DuckDB + Next.js',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}