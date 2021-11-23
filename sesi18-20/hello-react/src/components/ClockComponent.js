import React from 'react'
import { useEffect, useState } from 'react/cjs/react.development'

export default function ClockComponent() {
    const [date, setDate] = useState(new Date())
    const [date8, setDate8] = useState(new Date())

    useEffect(() => {
        const interval = setInterval(() => tick(), 1000)
        return function () {
            clearInterval(interval)
        }
    })
    // setInterval(() => tick(), 1000)

    function tick() {
        setDate(new Date())
        setDate8(new Date())
    }

    function dateplus8() {

        setDate8(date8.getTime() + (8 * 60 * 60 * 1000));

    }

    return (
        <>
            <div className="clock">
                <h1>function</h1>
                <h1>{date.toLocaleTimeString()}</h1>
                <h1>{date8.toLocaleTimeString()}</h1>
                <button onClick={dateplus8}>++</button>
            </div>
        </>
    )

}

