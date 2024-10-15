const express = require('express');
const app = express();
const PORT = 3000;

const products = [
    {
        id: 1,
        name: 'Sembako',
        description: "Description of Product 1. It's amazing!",
        price: 50000,
        imageUrl: 'sembako.png'
    },
    {
        id: 2,
        name: 'Alat Rumah',
        description: "Description of Product 2. You'll love it!",
        price: 70000,
        imageUrl: 'alat rumah.jpeg'
    },
    {
        id: 3,
        name: 'Product 3',
        description: "Description of Product 3. Must-have item!",
        price: 23900,
        imageUrl: 'maizena.avif'
    }
];

app.use(express.static('public'));

app.get('/api/products', (req, res) => {
    res.json(products);
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
