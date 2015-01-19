var InputTypes = Object.freeze({
    TEXT: "text",
    TIME: "time",
    PHONE: "phone number"                
});


function Info(name, type) {
    this.name = name;
    this.type = type;
    this.value = "";
    this.toHtml = function () {
        htmlList = new Array();
        htmlList.push('<div class="input-group"><label>' + this.name + '</label></div>');
        htmlList.push('<div class="input-group"><input type="'+ this.type +'" class="form-control"></div>');
        return htmlList;
    }
}

function Category(title) {
    this.title = title;
    this.info = new Array();
    this.people = new Array();
}

function Person(title){
    this.title = title;
    this.name = "";
    this.number = "";
    this.toHtml = function () {
        htmlList = new Array();
        htmlList.push('<div class="input-group"><label>' + this.title + '</label></div>');
        htmlList.push('<div class="input-group"><input type="text" class="form-control"></div>');
        htmlList.push('<div class="input-group"><input type="text" class="form-control" placeholder="555-555-5555"></div>');
        return htmlList;
    };
}

function Agent(){
    this.agent = new Person("agent");
    this.agency = "";
    this.toHtml = function () {
        htmlList = this.agent.toHtml();
        htmlList.push('<div class="input-group"><input type="text" class="form-control" placeholder="agency"></div>');
        return htmlList;
    };
}

function Talent(){
    this.name = "";
    this.agent = new Agent();
    this.time = "";
    this.note = "";
    this.toHtml = function () {
        htmlList = new Array();
        htmlList.push('<div class="input-group"><label>Talent</label></div>');
        htmlList.push('<div class="input-group"><div class="input-group-btn"><input type="time" class="form-control"></div><input type="text" class="form-control"></div>');
        htmlList = htmlList.concat(this.agent.toHtml());
        htmlList.push('<div class="input-group"><input type="text" class="form-control" placeholder="notes"></div>');
        return htmlList;
    }
}

var categories = ['Talent', 'Photo', 'Production', 'Wardrobe', 'Hair', 'Makeup',
                       'Art', 'Catering'];



var categoryObjects = new Array();


//talent
newCat = new Category(categories[0]);
newCat.people.push(new Talent());
categoryObjects.push(newCat);

//photo
newCat = new Category(categories[1]);
newCat.people.push(new Person("Photographer"));
newCat.people.push(new Person("Digital Tech"));
newCat.people.push(new Person("Assist 1"));
newCat.people.push(new Person("Assist 2"));
categoryObjects.push(newCat);

//production
newCat = new Category(categories[2]);
newCat.info.push(new Info("Company", InputTypes.TEXT));
newCat.people.push(new Person("Producer"));
newCat.people.push(new Person("Assist 1"));
categoryObjects.push(newCat);

//wardrobe
newCat = new Category(categories[3]);
newCat.people.push(new Person("Wardrobe Stylist"));
newCat.people.push(new Person("Assist 1"));
newCat.people.push(new Person("Assist 2"));
categoryObjects.push(newCat);

//hair
newCat = new Category(categories[4]);
newCat.people.push(new Person("Hair Stylist"));
newCat.people.push(new Person("Assist 1"));
newCat.people.push(new Person("Assist 2"));
categoryObjects.push(newCat);

//makeup
newCat = new Category(categories[5]);
newCat.people.push(new Person("Make-up Artist"));
newCat.people.push(new Person("Assist 1"));
newCat.people.push(new Person("Assist 2"));
categoryObjects.push(newCat);

//art
newCat = new Category(categories[6]);
newCat.people.push(new Person("Set Designer"));
newCat.people.push(new Person("Assist 1"));
newCat.people.push(new Person("Assist 2"));
categoryObjects.push(newCat);

//catering
newCat = new Category(categories[7]);
newCat.info.push(new Info("Company", InputTypes.TEXT));
newCat.people.push(new Person("Contact"));
categoryObjects.push(newCat);

for (var i = 1; i < categories.length; i++) {
    categoryObjects[i].info.push(new Info("time", InputTypes.TIME));
    categoryObjects[i].info.push(new Info("notes", InputTypes.TEXT));
}


$(document).ready(function () {
    console.log('ready!');


    var panels = new Array();
    for (var i = 0; i < categoryObjects.length; i++) {
        panels.push($('#collapse' + categories[i] + ' > .panel-body > .row > .col-lg-6'));
    }

    for (var i = 0; i < categoryObjects.length; i++) {
        for (var j = 0; j < categoryObjects[i].info.length; j++) {
            panels[i].append(categoryObjects[i].info[j].toHtml());
        }

        for (var j = 0; j < categoryObjects[i].people.length; j++) {
            var divs = categoryObjects[i].people[j].toHtml();
            for (var k = 0; k < divs.length; k++) {
                panels[i].append(divs[k]);
            }
            
        }
        
        panels[i].append('<button type="button" class="btn btn-success">Save</button>');

    }

    $(".btn-success").click(function () {
        saveValues($(this).parent());
    });
   
});

function saveValues(parent) {
    $(parent).find(".form-control").each(function (i) {
        console.log($(this).val());
    });
};