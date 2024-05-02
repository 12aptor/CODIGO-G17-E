export const createProduct = (req, res) => {
    console.log('Producto creado')
}

export const getAllProducts = (req, res) => {
    return res.json([
        {
            id: 1,
            name: 'Producto 1'
        },
        {
            id: 2,
            name: 'Producto 2'
        }
    ])
}