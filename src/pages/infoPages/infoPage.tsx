import Link from 'next/link'

export default function InfoPage() {
    return (
        <>
            <h1> This is the info page </h1>
            <h2> Go back to the <Link href = "/"> main page </Link></h2>
        </>

    )
}