import { useState, useEffect } from 'react'

export default function FetchComponent() {
    const [baseUrl] = useState('https://cat-fact.herokuapp.com')
    const [facts, setFacts] = useState([])

    useEffect(() => {
        fetch(`${baseUrl}/facts`)
            .then(response => response.json()
            ).then(result => setFacts(result))
    }, [])


    return (
        <>
            <div>
                {
                    facts.map(fact => (
                        <div key={fact._id}>
                            {fact.text}
                        </div>
                    ))
                }
            </div>
        </>
    )
}