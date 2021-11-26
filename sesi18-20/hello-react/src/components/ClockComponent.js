import React from 'react'
import { useEffect, useState } from 'react/cjs/react.development'
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css"



export default function ClockComponent() {
    const [date, setDate] = useState(new Date())
    const [date8, setDate8] = useState(new Date())

    useEffect(() => {
        const interval = setInterval(tick, 1000)
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

        setDate8(date8 + (8 * 60 * 60 * 1000));

    }

    return (
        <>
            <h5 className="text-decoration-line-through">the number mason! what do they mean</h5>
            <div className="clock">
                <h1>function</h1>
                <h1 className="badge bg-primary text-wrap">{date.toLocaleTimeString()}</h1>
                <h1 className="fst-italic">{date8.toLocaleTimeString()}</h1>
                <div className="card rounded-circle " style={{ width: "18rem", color: "black" }}>

                </div>
                <button className="btn btn-danger" onClick={dateplus8}>++</button>
                <hr />
            </div>
        </>
    )

}

