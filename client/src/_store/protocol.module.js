import { protocolService } from '../_services';
import { secretsService } from '../_services';
import { apiService } from '../_services';

const state = {
    protocols: {},
    processing: false
};

const actions = {
    getProtocols( {dispatch, commit, state }) {
        if (state.processing === false){
        apiService.protocols()
            .then(
                protocols => {
                    commit('protocolProcessing', protocols);
                    // console.log(protocols);
                    var user = JSON.parse(localStorage.getItem('user'));
                    var username = user.username;
                    protocols.forEach(element => {
                        console.log(element);
                        if (element.round == 3) {
                            var id = element.protocolID
                            var name = element.responder
                            var v = element.v

                            var result = protocolService.step3(name, v);
                            apiService.step3(
                                id,
                                username,
                                JSON.stringify(result)
                            );
                            console.log(`step3 sent: ${name}`);
                        }
                        else if (element.round == 4) {
                            var id = element.protocolID;
                            var name = element.iniciator;
                            var messages = JSON.parse(element.messagesForResponder);
                            var result = protocolService.step4(name, messages);
                            console.log(result)
                            apiService.step4(
                                id,
                                username,
                                result
                            );
                            console.log(`step4 sent: ${name}`)

                        }            
                    });
                    commit('protocolDone');
                }
            );
        }
    },

    startProt( { dispatch, commit, state }, { choice, name }) {
        apiService.startProt(name)
            .then(
                response => {
                    if (response.status == "false") {
                        var data;
                        var user = JSON.parse(localStorage.getItem('user'));
                        var username = user.username;
                        data = protocolService.step1(name, choice)

                        apiService.step1( 
                            username,
                            data[0],
                            data[1],
                            data[2],
                            data[3],
                            data[4],
                            data[5]
                        );
                        console.log(`step1 sent: ${name}`)
                    }
                    else {
                        var data;
                        var user = JSON.parse(localStorage.getItem('user'));
                        var username = user.username;
                        
                        console.log(response)
                        var encryptions = JSON.parse(response.encryptions);
                        var ac = response.iniciatorChoice;
                        var pubKey = JSON.parse(response.pubKey);
                        var otMessages = JSON.parse(response.iniciatorMessages);
                        var v = protocolService.step2(
                            name,
                            encryptions,
                            ac,
                            pubKey,
                            otMessages,
                            choice
                            );
                        apiService.step2(
                            response.protocolID,
                            username,
                            v
                        )
                        console.log(`step2 sent: ${name}`)
                    }
                }
            );
    }
};

const mutations = {
    protocolProcessing(state, protocols) {
        state = { protocols: protocols,
        processing: true };
    },
    protocolDone(state) {
        state = { processing: false}
    },
    // getDataFailure(state, error) {
    //     state.all = { error };
    // },
    // deleteRequest(state, id) {
    //     // add 'deleting:true' property to user being deleted
    //     state.all.items = state.all.items.map(user =>
    //         user.id === id
    //             ? { ...user, deleting: true }
    //             : user
    //     )
    // },
    // deleteSuccess(state, id) {
    //     // remove deleted user from state
    //     state.all.items = state.all.items.filter(user => user.id !== id)
    // },
    // deleteFailure(state, { id, error }) {
    //     // remove 'deleting:true' property and add 'deleteError:[error]' property to user 
    //     state.all.items = state.items.map(user => {
    //         if (user.id === id) {
    //             // make copy of user without 'deleting:true' property
    //             const { deleting, ...userCopy } = user;
    //             // return copy of user with 'deleteError:[error]' property
    //             return { ...userCopy, deleteError: error };
    //         }

    //         return user;
    //     })
    // },
    // updateRequest(state) {
    //     state.all = { loading: true };
    // },
    // updateSuccess(state) {
    //     state.all = { loading: false};
    // },
    // updateFailure(state, error) {
    //     state.all = { loading: false}; //TODO: handle the error message
    // },
    // getAllSuccess(state, users) {
    //     state.all = { items: users };
    // },
    // getAllFailure(state, error) {

    // },
};

export const protocol = {
    namespaced: true,
    state,
    actions,
    mutations
};