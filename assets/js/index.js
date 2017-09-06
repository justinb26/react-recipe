// Load react libs
var React = require('react')
var ReactDOM = require('react-dom')

// RecipeBox - Provides structure, loads the RecipeList and RecipeForm
var RecipeBox = React.createClass({
    render: function() {
        return (
            <div className="container">
                <RecipesList url='/api/recipes' pollInterval={1000} />
                <RecipeForm/>
            </div>
        );
    }
});


var RecipeTag = React.createClass({
    
    getInitialState: function() {
        return { 
            value: "foo", 
            size: 3,
            isEditing: false
        };
    },

    handleClose: function(e) {
        // e.preventDefault();
        // e.stopPropagation();
        
        // this.setState({
        //     isEditing: false,
        // });
    },

    handleKeypress: function(e) {
        // Enter pressed, end editing
        if (e.which == 13 || e.keyCode == 13) {
            this.setState({isEditing: false});
        }
    },

    handleChange: function(e) {
        this.setState(
            {
                value: e.target.value, 
                size: e.target.value ? e.target.value.length : 3
            }
        );
    },

    handleEdit: function(e) {
        this.setState(
            {
                isEditing: true,
            });
    },


    render: function() {

        var isEditing = this.state.isEditing;
        var currentValue = this.state.value.toString();

        return (
            <div className="chip">
                
                {isEditing ? (
                    <input type="textbox" size={this.state.size} value={this.state.value} onChange={this.handleChange} onKeyPress={this.handleKeypress}/>
                ) : (
                    <span onClick={this.handleEdit}>{currentValue}</span>
                )}
                
                <i className="close material-icons" onClick={this.handleClose}>close</i>
            </div>
        );
    }
});




var RecipeForm = React.createClass({
    clickme: function() {
        var randomString = random(100).toString();
        $.post({
            url: "/api/recipes",
            data: {
                title: "fsdfsdfds" + randomString,
                description: "fddfsdfd"
            },
            success: function() {
                alert("fuck you");
                location.reload();
            }
        });
    },
    render: function(){
        return (
            <a className="btn btn-floating pulse"><i className="material-icons">menu</i></a>
        );
    }
});

// Loops through a "recipes" object, rendering Recipe templates for each one
var RecipesList = React.createClass({

    // Initialize empty data structure
    getInitialState: function() { 
        return {
            data: []
        };
    },

    // Custom: Performs an Ajax call to the /api/recipes endpoint to get a "recipes" object
    loadRecipesFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    // When component is loaded, perform an initial load from the server, 
    //   then set up a timer to do it periodically
    componentDidMount: function() { // ui event stuff
        this.loadRecipesFromServer();
        setInterval(this.loadRecipesFromServer,
                    this.props.pollInterval)
    },


    // Generate output by mapping recipe objects to Recipe template
    render: function() {
        var recipes = this.state.data.map(function(recipe, index) {
            return (
                <Recipe key={index} id={index} title={recipe.title} ingredients={recipe.ingredients}/>
            );
        }.bind(this));

        return (
            <div className="container">
                {recipes}
            </div>
        )
    }
});


var Recipe = React.createClass({

    // Initialize empty data structure
    getInitialState: function() {
        return {
            // isEditing: false,
            tags: ["foo", "bar"] // each tag is a string
        };
    },

    componentDidMount: function() {
    },



    handleClick: function(e) {
        var myTags = this.state.tags;
        myTags.push("baz")

        this.setState({
            tags: myTags
            // isEditing: true,
            // tags: myTags
        });

        //$('.card').append('<div class="chip">foo</div>');
    },
    render: function() {
        var title = this.props.title;
        
        var ingredients = this.props.ingredients.map(function(ingredient, index) {
            return <Ingredient key={index} stuff={ingredient}/>;
        });



        var editingChips = this.state.tags.map(function(tag, index){
            return <RecipeTag key={index} name={tag}/>
        });

        // ? (
        //     <RecipeTag/>
        // ) : "";



        return (
            <div className="card blue-grey darken-1">
                <div className="card-content white-text">
                    <span className="card-title">{title}</span>
                    <div>
                        Ingredients:
                        <ul>
                            {ingredients}
                        </ul>
                    </div>

                    
                    <div>
                        <a className="btn-floating btn-small waves-effect waves-light" onClick={this.handleClick}><i className="material-icons">add</i></a>
                    </div>

                    {editingChips}


                </div>
            </div>
        );
    }
});



var Ingredient = React.createClass({
    render: function() {
        return <li>{this.props.stuff}</li>
    }
});



ReactDOM.render(<RecipeBox/>, document.getElementById('container'))
