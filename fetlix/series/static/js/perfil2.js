const API_URL ="http://127.0.0.1:8000";

const user_id = JSON.parse(document.getElementById('user_id').textContent);

fetch(`${API_URL}/empresas/empresa/${user_id}`)
        .then((response)=>response.json())
        .then((r)=>{

        let imagenPerfil = document.getElementById("fotoPerfil")
        imagenPerfil.src=r.imagen

        fetch(`${API_URL}/productos/producto/empresa/${r.id}`)
            .then((response)=>response.json())
            .then((response)=>{
                response.forEach((pro)=>{

                    const productos = document.createElement('div')
                    const idProductos = document.createAttribute('id')
                    idProductos.value='idProductos'
                    productos.setAttributeNode(idProductos)

                    const dato = document.createElement('div')
                    let comentarios = document.createElement('div')

                    //---------
                    let imagen = document.createElement('img')
                    let foto = document.createAttribute('src')

                    foto.value=`${pro.imagen}`
                    imagen.setAttributeNode(foto)

                    //let salto= document.createElement('br')

                    //---------
                    let nombre = document.createElement('p')
                    let nombreIcono = document.createElement('span')
                    nombreIcono.className='fas fa-box '
                    nombre.appendChild(nombreIcono)
                    nombre.appendChild(
                        document.createTextNode(" "+`${pro.nombre}`)
                    );

                    let empresa = document.createElement('p')
                    let empresaIcono = document.createElement('span')
                    empresaIcono.className='fas fa-user'
                    empresa.appendChild(empresaIcono)
                    empresa.appendChild(
                        document.createTextNode(" "+`${pro.empresa}`)
                    );


                    let precio = document.createElement('p')
                    let precioIcono = document.createElement('span')
                    precioIcono.className='fas fa-money-bill'
                    precio.appendChild(precioIcono)
                    precio.appendChild(
                        document.createTextNode(" "+`${pro.precio}`+" €")
                    );


                    let mg = document.createElement('i')
                    let idMg = document.createAttribute('id')
                    idMg.value='meGusta'
                    mg.setAttributeNode(idMg)
                    mg.appendChild(
                        document.createTextNode(" "+`${pro.num_likes}`)
                    );


                    let mgIcono = document.createElement('span')
                    let funcionMg = document.createAttribute('onclick')
                    let idIconoMg = document.createAttribute('id')
                    idIconoMg.value='iconoMeGusta'
                    funcionMg.value='doLike()'
                    mgIcono.setAttributeNode(funcionMg)
                    mgIcono.setAttributeNode(idIconoMg)
                    mgIcono.className='fas fa-heart '

                    //---------

                    let descripcion = document.createElement('p')
                    let idDescripcion= document.createAttribute('id')
                    let descripcionIcono = document.createElement('span')
                    idDescripcion.value='descripcion'
                    descripcionIcono.className='fas fa-scroll'
                    descripcion.appendChild(descripcionIcono)
                    descripcion.appendChild(
                        document.createTextNode(" "+pro.descripcion)
                    );
                    descripcion.setAttributeNode(idDescripcion)
                    descripcion.className='descripcion'
                    //---------

                    //dato.appendChild(nombreIcono)
                    dato.appendChild(nombre)
                    dato.appendChild(empresa)
                    dato.appendChild(precio)
                    dato.appendChild(mgIcono)
                    dato.appendChild(mg)

                    productos.appendChild(imagen)
                    productos.appendChild(dato)
                    productos.appendChild(descripcion)
                    
                    imagen.className = 'foto-producto'
                    dato.className = 'datos'
                    productos.className= 'producto'


                    document.body.appendChild(productos);
                })


        });
})