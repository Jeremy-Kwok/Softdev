const viewWidth = 500;
const viewHeight = 500;
const mapWidth = 1500;
const mapHeight = 3000;
const scaleRatioX = 0.2; //viewWidth / mapWidth;
const scaleRatioY = 0.2; //viewHeight / mapHeight;
let islandsGroup;

var config = {
    type: Phaser.AUTO,
    
    scale: {
        //mode: Phaser.Scale.FIT,
        parent: "canvas",
        width: viewWidth,
        height: viewHeight,
    },
    physics: {
        default: 'arcade',
        arcade: { 
            gravity: { y: 1000 }, // Set the gravity value
            debug: true // Set to true to show physics bodies
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);

function preload() {
    //Preload sprites
    this.load.image("kirby", "static/assets/kirby.png");   // 689x685
    this.load.image("ground", "static/assets/ground.png"); // 333x32
    this.load.image("goal", "static/assets/goal.png");     // 512x512
    this.load.image("lava", "static/assets/lava.png");     // 487x103
}

function create() {

    //Create lava floor
    lava = this.add.sprite(mapWidth/2, mapHeight, "lava"); //this.sys.game.config.height-200, "lava");
    lava.setScale(10, 1);

    //Create islandsGroup
    islandsGroup = this.physics.add.staticGroup();

    //Create first floating island
    var firstIsland = islandsGroup.create(mapWidth/2, mapHeight-32, "ground");
    firstIsland.setSize(200, 42);
    firstIsland.displayWidth = 200;

    //Create floating islands
    const islands = generateIslands();
    islands.forEach((island) => {
        createIsland(island.x, island.y, island.width, 32);
    });

    //create goal
    goal = this.physics.add.sprite(900,1800, "goal");
    goal.setScale(0.2,0.2);

    //Create kirby
    kirby = this.physics.add.sprite(mapWidth/2, 2700, "kirby");
    kirby.setScale(0.2,0.2);

    //Make bouncy kirby
    kirby.setBounce(0.2);

    //Laws of Physics
    //kirby.setCollideWorldBounds(true);

    //Enable cursor keys for kirby movement
    cursors = this.input.keyboard.createCursorKeys();

    //Let colliders
    this.physics.add.collider(kirby, islandsGroup);
    this.physics.add.collider(goal, islandsGroup);

    //this.cameras.main.setOrigin(this.sys.game.config.width/2, 2700)
    this.cameras.main.setBounds(0, 0, mapWidth, mapHeight);

    this.cameras.main.setViewport(0, 0, 500, 500);
    this.cameras.main.setZoom(Math.min(scaleRatioX, scaleRatioY));

    //Make camera focus kirby
    this.cameras.main.startFollow(kirby);

}

function update() {

    //Kirby Freeze
    kirby.setVelocityX(0);

    //Kirby MOVE
    if (cursors.left.isDown){
        kirby.setVelocityX(-250);
    } else if (cursors.right.isDown){
        kirby.setVelocityX(250);
    }

    if (cursors.up.isDown){
        if (kirby.body.touching.down){
            kirby.setVelocityY(-1000);
        }
    } 

    //Adjust camera according to kirby's height
    this.cameras.main.scrollY = kirby.y - this.cameras.main.height/2;

    //Check if the Kirby reaches the goal
    if (Phaser.Geom.Intersects.RectangleToRectangle(kirby.getBounds(), goal.getBounds())){
        winGame();
    }

    if (Phaser.Geom.Intersects.RectangleToRectangle(kirby.getBounds(), lava.getBounds())){
        loseGame();
    }
}

function generateIslands() {
    var islands = [];

    var islandX;
    var islandY;
    let lastIslandX = mapWidth/2;
    let lastIslandY = mapHeight - 32;
    const maxGap = 500;
    const minGap = 200;
    var islandWidth;
    var lastIslandWidth = 150;
    var ct = 0;

    while (lastIslandY > 0){
        //333x32

        islandWidth = Math.floor(Math.random() * 200) + 100; //Random width btwn 100 and 300
        var gap = Math.floor(Math.random() * (maxGap - minGap + 1)) + minGap;
        var fiftyChance = (Math.random() < 0.5 ? -1 : 1);

        //keep islandX within map bounds
        islandX = lastIslandX + (fiftyChance * (lastIslandWidth + gap));

        /*
        while (islandX < 0 || islandX + islandWidth > mapWidth){
            islandX = lastIslandX + (fiftyChance * (lastIslandWidth + gap));
        }
        */

        
        if (islandX < 0){
            islandX = lastIslandX + (lastIslandWidth + gap);
        }
/*
        if(islandX + islandWidth > mapWidth){
            islandX = lastIslandX - (lastIslandWidth + gap);
        }
        */

        islandY = lastIslandY - Math.floor(Math.random() * 100 + 200);

        //push values to constructor
        islands.push({
            x: islandX,
            y: islandY,
            width: islandWidth,
            height: 32
        });

        //push the creation data of last island
        lastIslandX = islandX;
        lastIslandY = islandY;
        lastIslandWidth = islandWidth;
    }
    
    return islands;
}

function createIsland(x, y, width, height) {
    console.log("x: " + x + " y: " + y + " width: " + width + " height " + height);
    const island = islandsGroup.create(x, y, "ground");
    island.setSize(width, height);
    island.displayWidth = width;
}

function winGame() {
    console.log("YOU FINALLY WON!");
}

function loseGame() {
    console.log("You died. You suck!");
}

