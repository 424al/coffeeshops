import React, {Component} from "react";


class Promise extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            loaded: false,
            placeholder: "Loading"
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8000/api/shops/")
            .then(response => {
                if (response.status > 400) {
                    return this.setState(() => {
                        return {placeholder: "Something went wrong!"};
                    });
                }
                return response.json();
            })
            .then(data => {
                this.setState(() => {
                    return {
                        data,
                        loaded: true
                    };
                });
            });
    }

    render() {
        return (
            <div id={'djangodata'}>
                <ul>
                    {this.state.data.map(contact => {
                        return (
                            <li key={contact.name}>
                                {contact.name} - {contact.name}
                            </li>
                        );
                    })}
                </ul>
            </div>
        );
    }
}

export default Promise;
