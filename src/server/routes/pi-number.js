//Imports
const express = require('express')

//Config
const router = express.Router()

//Routes
router.get('/',(req, res) =>{
    res.send('Works!!!')
})

//Export
module.exports = router