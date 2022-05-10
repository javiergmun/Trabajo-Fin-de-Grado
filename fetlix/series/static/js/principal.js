const API_URL ="https://jsonplaceholder.typicode.com";
const HTMLResponse = document.querySelector("#datos");
const tpl=document.createElement;

fetch(`${API_URL}/users`)
    .then((response)=>response.json())
    /*.then((response)=>{
        response.forEach((user)=>{
            let nombre = document.getElementById('nombrecito')
            nombre.append(`${user.name}`)
            HTMLResponse.appendChild(nombre)
        })      
    })
    .then((response) =>console.log );*/