import { Menubar } from "primereact/menubar";
import NavBar from "../ui/NavBar";
import { Toaster } from "react-hot-toast";
import { Guards } from "meutcc/core/constants";
import { useAuth } from "meutcc/core/context/AuthContext";

export const AppLayout = ({ children, guards }) => {

    const { user } = useAuth();

    const typesMenu = {
        Todos: [
            { label: 'Inicio', icon: 'pi pi-fw pi-home', url: '/' },
            { label: 'Meus TCCs', icon: 'pi pi-fw pi-book', url: '/meus-tccs' },
        ],
        Estudante: [
        ],
        Coordenador: [
            { label: 'Configurações', icon: 'pi pi-fw pi-cog', url: '/painel-configuracoes' },    
        ]
    }

    const items = typesMenu.Todos.concat(typesMenu[user?.resourcetype] || []);

    const isUserAuth = !!user || false;

    return (
        <div className='bg-gray-100 min-h-screen'>
            <Toaster
                position="top-center"
                reverseOrder={false}
            />
            <NavBar auth={isUserAuth} />

            <div style={{backgroundColor: '#f9fafb'}}>
                {
                    isUserAuth &&
                    <Menubar model={items} style={{borderWidth: 0}} className='max-w-screen-lg mx-auto' />
                    ||
                    <div>
                        <div className='max-w-screen-lg mx-auto text-gray-600 text-2xl p-6 ps-10'>Meu TCC IFRS Campus Restinga</div>
                    </div>
                }
            </div>

            {children}

            <footer className='bg-gray-800 text-white text-center py-9 mt-10'>
                <p>Instituto Federal do Rio Grande do Sul – Campus Restinga</p>
                <p>Rua Alberto Hoffmann, 285 | Bairro Restinga | CEP: 91791-508 | Porto Alegre/RS</p>
                <p>Créditos do site:</p>
                <p>Alunos: Bruno Padilha, Carlos Eduardo, Carlos Rafael, Cid Monza, Matheus Machado, Matheus Costa Krenn</p>
                <p>Professores: Ricardo dos Santos, Eliana Pereira</p>
                <p>Coordenador: Roben Lunardi - ads@restinga.ifrs.edu.br</p>
            </footer>
        </div>
    );
};