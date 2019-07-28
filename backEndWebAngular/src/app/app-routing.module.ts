import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ChartsComponent } from './charts/charts.component';
import { IndexComponent } from './index/index.component';
import { ElementsComponent } from './elements/elements.component';
import { IconsComponent } from './icons/icons.component';
import { NotificationsComponent } from './notifications/notifications.component';
import { PanelsComponent } from './panels/panels.component';
import { TablesComponent } from './tables/tables.component';
import { TypographyComponent } from './typography/typography.component';


const routes: Routes = [
  {
    path: '',
    component:IndexComponent
  },
  {
    path: 'index',
    component:IndexComponent
  },
  {
    path: 'charts',
    component:ChartsComponent
  },
  {
    path: 'elements',
    component:ElementsComponent
  },
  {
    path: 'icons',
    component:IconsComponent
  },
  {
    path: 'notifications',
    component:NotificationsComponent
  },
  {
    path: 'panels',
    component:PanelsComponent
  },
  {
    path: 'tables',
    component:TablesComponent
  },
  {
    path: 'typography',
    component:TypographyComponent
  },


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 

}
