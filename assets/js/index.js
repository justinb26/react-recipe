var React = require('react')
var ReactDOM = require('react-dom')


var RecipesList = React.createClass({
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

    getInitialState: function() { // initialize state
        return {data: []};
    },

    componentDidMount: function() { // ui event stuff
        this.loadRecipesFromServer();
        setInterval(this.loadRecipesFromServer,
                    this.props.pollInterval)
    },


    render: function() { // generate output
        if (this.state.data) {
            console.log('DATA!')

            var recipeNodes = this.state.data.map(function(recipe){
                return <li> {recipe.title} - bar {recipe.ingredients} foo </li>
            })

        }


        // var del = this.props.onDelete;
        var index = -1;
        var recipes = this.state.data.map(function(recipe) {
            index++;
          return <Recipe key={index} id={index} title={recipe.title} ingredients={recipe.ingredients}/>;
            //recipe={recipeData} bindToModal={this.props.bindToModal} 
            //onEdit={this.props.onEdit} onDelete={del}/>;
        }.bind(this));


        return (
            <div>
                <ul>
                    {recipes}
                </ul>
            </div>
        )
    }
});



var Recipe = React.createClass({
    componentDidMount: function() {
        
    },
    render: function() {
        var title = this.props.title;
        
        var ingredients = this.props.ingredients;
        console.log(ingredients);

        return (
            <li>
                Recipe: {title}<br/>
                Ingredients: {ingredients}<br/>
            </li>
        );
    }
});


ReactDOM.render(<RecipesList url='/api/recipes'  pollInterval={1000} />,
    document.getElementById('container'))
