import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { HttpService } from './http.service';
import { HttpClientModule } from '@angular/common/http';
import axios from 'axios';


export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), HttpService, HttpClientModule]
};