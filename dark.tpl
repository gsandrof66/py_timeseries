{% extends 'lab/index.html.j2' %}

{% block html_head %}
    {{ super() }}
    <style>
        
        .jp-Notebook {
            background-color: #000000;
            color: #000000;
        }
        .jp-Cell {
            background-color: #000000;
            color: #ffffff;
        }
        .jp-CodeCell .jp-InputArea-editor {
            background-color: #000000;
            color: #ffffff;
        }
        pre {        
            background-color: #1e1e1e;
            color: #ffffff;
            font-weight: bold;
        }
        /* Override pandas DataFrame styles */
        table.dataframe {
            background-color: #000000;
            color: #ffffff;
            border-collapse: collapse;
            width: 100%;
        }

        
    </style>
{% endblock html_head %}
