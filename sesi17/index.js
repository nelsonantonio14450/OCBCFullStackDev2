var promise = require('promise');


function showInTerminal(message) {
    console.log(message + 'asdadasd')
}

async function greeting(name, callback = showInTerminal) {
    const value = 'haros' + name


    // return new promise((resolve, reject) => {
    //     

    //     resolve("selesai")
    // })

    setTimeout(() => callback(value), 1500)
    return "asdasdasdasdad" //message
}

greeting("hasageee").then((messages) => console.log(messages)).then(err => { throw err })
    .then((messages) => console.log(messages)).then((messages) => console.log(messages))
    .catch(err => console.error(err))