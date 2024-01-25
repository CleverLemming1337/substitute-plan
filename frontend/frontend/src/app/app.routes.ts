import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { SubstComponent } from './subst/subst.component';
import { NotFoundComponent } from './not-found/not-found.component';

export const routes: Routes = [
    { path: "", component: HomeComponent },
    { path: "subst", component: SubstComponent },
    { path: "subst/:filter", component: SubstComponent },
    { path: "subst/:filter/:param", component: SubstComponent },
    { path: "**", component: NotFoundComponent }
];
