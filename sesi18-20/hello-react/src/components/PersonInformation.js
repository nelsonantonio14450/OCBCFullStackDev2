import React, { useEffect, useState } from 'react'
import Quote from './Quote'


function PersonInformation() {

    const [name, setName] = useState("asdasd")
    const [age, setAge] = useState(17)
    const [quote, setQuote] = useState("asdadsad")


    const changeName = () => {
        const newName = name + 2
        setName(newName)
    }

    const changeAge = () => {
        setAge(age + 1)
    }

    const changeQuote = () => {
        setQuote(quote + "asda")
    }

    useEffect(() => {
        document.title = "my name is " + name
    }, [age, quote])

    // const [personData, setPersonData] = useState({
    //     name: "asdasd",
    //     age: 177,
    //     quote: "asdasdad123123"
    // })

    // const changeName = () => {
    //     const newName = personData.name + 2
    //     setPersonData({
    //         ...personData,
    //         name: newName
    //     })
    // }

    return (
        <>
            <h1>person info</h1>
            <div>
                <span>name: {name}</span><br />
                <span>Age: {age}</span><br />
                <span>Quote: </span>
                <Quote quote={quote} />
                <button onClick={changeName}>P</button>
                <button onClick={changeAge}>age</button>
                <button onClick={changeQuote}>qt</button>
            </div>
        </>
    )
}



// export class PersonInformation extends Component {

//     constructor() {
//         super()
//         // this.state = {
//         //     name: "septhan",
//         //     age: 17,
//         //     quote: "asdasdadasd"
//         // }
//     }
//     render() {
//         return (
//             <>
//                 <h1>person info</h1>
//                 <div>
//                     <span>name: {personData.name}</span><br />
//                     <span>Age: {personData.age}</span><br />
//                     <span>Quote: </span>
//                     <Quote quote={personData.quote} />
//                 </div>
//             </>
//         )
//     }

// }

export default PersonInformation