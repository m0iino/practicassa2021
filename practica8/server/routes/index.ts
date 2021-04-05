import { json } from "express";
var express = require('express');
var db = require('../db/index');
var router = express.Router();

router.get('/listar', async (req, res, next) => {
    try{
        let results = await db.all();
        res.json(results);
        
    } catch(e) {
        console.log(e);
        res.sendStatus(500);
    }
});

module.exports = router