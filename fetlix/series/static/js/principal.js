const API_URL ="https://jsonplaceholder.typicode.com";

fetch(`${API_URL}/users`)
    .then((response)=>response.json())
    .then((response)=>{
        response.forEach((user)=>{

            const productos = document.createElement('div')
            const dato = document.createElement('div')
            const comentarios = document.createElement('div')

            //---------
            let imagen = document.createElement('img')
            /*imagen.appendChild(
                document.createAttribute('src').value(`${user.imagen}`)
            )*/

            //---------
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

            //---------

            let textComentarios = document.createElement('p')
            textComentarios.appendChild(
                document.createTextNode("Comentarios: ")
            );
            //---------

            let botonComentar = document.createElement('input')
            let tipo = document.createAttribute('type')
            let nombreBoton = document.createAttribute('value')
            tipo.value='button',
            nombreBoton.value="Comentar"
            botonComentar.setAttributeNode(tipo)
            botonComentar.setAttributeNode(nombreBoton)


            fetch(`${API_URL}/users`)
                .then((response)=>response.json())
                .then((response)=>{
                    response.forEach((comentary)=>{

                    
                    const comentario = document.createElement('div')

                    let usuarioPost = document.createElement('p')
                    usuarioPost.appendChild(
                    document.createTextNode(`${comentary.website}`)
                    );

                    let valoracion = document.createElement('p')
                    valoracion.appendChild(
                    document.createTextNode(`${comentary.email}`)
                    );

                    comentario.appendChild(usuarioPost)
                    comentario.appendChild(valoracion)

                    comentarios.appendChild(comentario)

                    comentario.className='comentario'
                    
            });
            //---------

            dato.appendChild(nombre)
            dato.appendChild(empresa)
            dato.appendChild(precio)
            dato.appendChild(mg)
            

        
            productos.appendChild(imagen)
            productos.appendChild(dato)
            productos.appendChild(textComentarios)
            productos.appendChild(comentarios)
            productos.appendChild(botonComentar)

            

            //---------
            botonComentar.className = 'boton-comentar'
            comentarios.className = 'comentarios'
            imagen.className = 'foto-producto'
            dato.className = 'datos'
            productos.className= 'producto'

            
            document.body.appendChild(productos);
        })

            
    });
})