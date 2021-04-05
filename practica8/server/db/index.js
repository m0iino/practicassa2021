const mysql = require('mysql');

const con = mysql.createConnection({

  
    host: 'db-mysql',
    port: '3306',
    user: 'root',
    password: '1234',
    database: 'practica8'
});
let proyectobd = {};
proyectobd.all = () => {
    
        
    return new Promise((resolve, reject) => {
        const query = "SELECT * FROM tabla1;";
        con.query(query, (err, res) => {
        if (err) throw err;           

        resolve(res);
        });
    });


};

module.exports = proyectobd;