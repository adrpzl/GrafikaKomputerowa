function pyramid(sides) {
    const baseVertices = [];
    const indices = [];
    const vertexNormals = [];
    const vertexTextureCoords = [];
    const apex = [0, 0, 1]; // Wierzchołek ostrosłupa
    const angleStep = (2 * Math.PI) / sides;

    // Generowanie wierzchołków podstawy
    for (let i = 0; i < sides; i++) {
        const angle = i * angleStep;
        const x = Math.cos(angle);
        const y = Math.sin(angle);
        baseVertices.push([x, y, 0]);
        vertexTextureCoords.push([(x + 1) / 2, (y + 1) / 2]);
    }

    // Dodanie wierzchołka ostrosłupa
    baseVertices.push(apex);
    vertexTextureCoords.push([0.5, 0.5]);

    // Generowanie ścian bocznych
    for (let i = 0; i < sides; i++) {
        const next = (i + 1) % sides;
        indices.push(i, next, sides); // Trójkąty łączące podstawę z wierzchołkiem
    }

    // Generowanie podstawy
    for (let i = 1; i < sides - 1; i++) {
        indices.push(0, i, i + 1);
    }

    // Normale (przybliżone)
    for (let i = 0; i < baseVertices.length; i++) {
        vertexNormals.push([0, 0, 1]);
    }

    return {
        vertexPositions: new Float32Array(baseVertices.flat()),
        vertexNormals: new Float32Array(vertexNormals.flat()),
        vertexTextureCoords: new Float32Array(vertexTextureCoords.flat()),
        indices: new Uint8Array(indices),
    };
}