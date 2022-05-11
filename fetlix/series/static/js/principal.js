const API_URL ="https://jsonplaceholder.typicode.com";

fetch(`${API_URL}/users`)
    .then((response)=>response.json())
    .then((response)=>{
        response.forEach((user)=>{

            const productos = document.createElement('div')
            const dato = document.createElement('div')

            let nombre = document.createElement('p')
            nombre.appendChild(
                document.createTextNode(`${user.name}`)
            );

            let empresa = document.createElement('p')
            empresa.appendChild(
                document.createTextNode(`${user.username}`)
            );

            let precio = document.createElement('p')
            precio.appendChild(
                document.createTextNode(`${user.email}`)
            );

            let mg = document.createElement('p')
            mg.appendChild(
                document.createTextNode(`${user.phone}`)
            );
            
            dato.appendChild(nombre)
            dato.appendChild(empresa)
            dato.appendChild(precio)
            dato.appendChild(mg)

            productos.appendChild(dato)

            dato.className = 'datos'
            productos.className= 'producto'

            

            document.body.appendChild(productos);
        })

            
    });
    