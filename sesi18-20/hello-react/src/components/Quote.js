import React, { useEffect, useState } from 'react'

function Quote(props) {
    const [quote, setQuote] = useState(props.quote)

    useEffect(() => {
        setQuote(props.quote)
    }, [props.quote])
    return (
        <>
            <blockquote>
                {quote}
            </blockquote>
        </>
    )
}

export default Quote