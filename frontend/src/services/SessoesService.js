import { apiClient } from "meutcc/libs/api"

async function getSessoesPendentes() {
    return apiClient.get('/app/sessoes-futuras').then((response) => response.data);
}

async function getSessoesPendentesOrientador() {
    return apiClient.get('/app/sessoes-futuras-orientador').then((response) => response.data);
}

async function getSessoesPendentesCoordenador() {
    return apiClient.get('/app/sessoes-futuras-coordenador').then((response) => response.data);
}

async function putEditarSessao(data) {
    return apiClient.put('/app/editar-sessao', data).then((response) => response.data);
}

async function putEditarSessaoOrientador(data) {
    return apiClient.put('/app/editar-sessao-orientador', data).then((response) => response.data);
}

async function postNovaSessao(data) {
    return apiClient.post('/app/nova-sessao', data).then((response) => response.data);
}

async function getSessoesFuturas() {
    return apiClient.get(`/app/sessoes-futuras`).then((response) => response.data);
}

async function avaliarPrevia(sessaoId, data) {
    return apiClient.post(`/app/avaliar-previa/${sessaoId}/`, data).then((response) => response.data);
}


export default {
    getSessoesPendentes,
    getSessoesPendentesOrientador,
    getSessoesPendentesCoordenador,
    putEditarSessao,
    putEditarSessaoOrientador,
    postNovaSessao,
    getSessoesFuturas,
    avaliarPrevia,
}