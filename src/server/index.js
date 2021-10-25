//Imports
const express = require('express')
const piNumber = require('./routes/pi-number')

//Config
const app = express()
const port = 3000

//Routes
app.get('/',(req,res)=>{
    res.send('Hello World!!!')
})

app.use(express.static('public'))
app.use('/pi-number', piNumber)

//Others
app.listen(port, ()=>{
    console.log(`pi_number_api listening at port ${port}`)
})
