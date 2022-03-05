#importing the libraries
import json
import plotly
import plotly.express as px
from sklearn.cluster import KMeans
from flask import Flask, request, render_template


app = Flask(__name__)

dataset = px.data.iris()
x = dataset.iloc[:, :4].values

#Applying kmeans to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 500, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)

df = px.data.iris()
df['k_means'] = y_kmeans

#Visualization in the app
@app.route('/')
def charts():
    header="MACHINE LEARNING TASK FROM COSMOS"

    title1="Visual Representation 1"
    fig_1 = px.treemap(df, path=['k_means','species','sepal_length'], color='sepal_length')
    graphJSON_1 = json.dumps(fig_1, cls=plotly.utils.PlotlyJSONEncoder)
    description1 = """
    A visual representation of clusters that are found by applying K-means clustering on the Iris dataset.
    The first parent is default, which contains the cluster numbers as child.
    The next level is the species name of the samples which are colored with their sepal length here.
    """

    title2="Visual Representation 2"
    fig_2 = px.treemap(df, path=['k_means','species','sepal_width'], color='sepal_width')
    graphJSON_2 = json.dumps(fig_2, cls=plotly.utils.PlotlyJSONEncoder)
    description2 = """
    A visual representation of clusters that are found by applying K-means clustering on the Iris dataset.
    The first parent is default, which contains the cluster numbers as child.
    The next level is the species name of the samples which are colored with their sepal width here.
    """

    title3="Visual Representation 3"
    fig_3 = px.treemap(df, path=['k_means','species','petal_length'], color='petal_length')
    graphJSON_3 = json.dumps(fig_3, cls=plotly.utils.PlotlyJSONEncoder)
    description3 = """
    A visual representation of clusters that are found by applying K-means clustering on the Iris dataset.
    The first parent is default, which contains the cluster numbers as child.
    The next level is the species name of the samples which are colored with their petal length here.
    """

    title4="Visual Representation 4"
    fig_4 = px.treemap(df, path=['k_means','species','petal_width'], color='petal_width')
    graphJSON_4 = json.dumps(fig_4, cls=plotly.utils.PlotlyJSONEncoder)
    description4 = """
    A visual representation of clusters that are found by applying K-means clustering on the Iris dataset.
    The first parent is default, which contains the cluster numbers as child.
    The next level is the species name of the samples which are colored with their petal width here.
    """

    return render_template('index.html',
                           header = header,
                           title1 = title1,
                           title2 = title2,
                           title3 = title3,
                           title4 = title4,
                           graphJSON_1 = graphJSON_1,
                           graphJSON_2 = graphJSON_2,
                           graphJSON_3 = graphJSON_3,
                           graphJSON_4 = graphJSON_4,
                           description1 = description1,
                           description2 = description2,
                           description3 = description3,
                           description4 = description4)


if __name__ == "__main__":
    app.run(debug=True)